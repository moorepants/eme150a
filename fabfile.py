from fabric.api import *
import fabric.contrib.project as project
import os
import shutil
import sys
import SocketServer
import datetime

from pelican.server import ComplexHTTPRequestHandler

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'

# Github Pages configuration
env.github_pages_branch = "gh-pages"

# Port for `serve`
PORT = 8000

def clean():
    """Remove generated files"""
    if os.path.isdir(DEPLOY_PATH):
        shutil.rmtree(DEPLOY_PATH)
        os.makedirs(DEPLOY_PATH)

def build():
    """Build local version of site"""
    local('pelican -s pelicanconf.py')

def rebuild():
    """`clean` then `build`"""
    clean()
    build()

def regenerate():
    """Automatically regenerate site upon file modification"""
    local('pelican -r -s pelicanconf.py')

def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir(env.deploy_path)

    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve():
    """`build`, then `serve`"""
    build()
    serve()

def preview():
    """Build production version of site"""
    local('pelican -s publishconf.py')

def cf_upload():
    """Publish to Rackspace Cloud Files"""
    rebuild()
    with lcd(DEPLOY_PATH):
        local('swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
              '-U {cloudfiles_username} '
              '-K {cloudfiles_api_key} '
              'upload -c {cloudfiles_container} .'.format(**env))

@hosts(production)
def publish():
    """Publish to production via rsync"""
    local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True,
        extra_opts='-c',
    )

def gh_pages():
    """Publish to GitHub Pages"""
    clean()
    local('pelican -s publishconf.py')
    local("ghp-import -n -b {github_pages_branch} {deploy_path}".format(**env))
    local("git push origin {github_pages_branch}".format(**env))

def build_homework():
    """Constructs the homework rst page and a pdf."""
    hw_dir = 'homework'
    hw_nums = [name for name in os.listdir(hw_dir) if
               os.path.isdir(os.path.join(hw_dir, name))]
    assigned_dates = {'01': '2015/09/28',
                      '02': '2015/10/05',
                      '03': '2015/05/12',
                      '04': '2015/10/19',
                      '05': '2015/11/02',
                      '06': '2015/11/09',
                      '07': '2015/11/16',
                      '08': '2015/11/23'}
    pdf_text = \
"""\
================================
EME 150A Fall 2015 Homework #{}
================================

:date: {}

**DUE: {} before class in Box D in the MAE department.**

"""

    web_text = \
"""\
:title: Homework #{}
:subtitle: {}
:status: hidden

**DUE: {} before class in Box D in the MAE department.**

`PDF Version <{{attach}}/materials/hw-{}.pdf>`_
"""
    preamble = r'\usepackage[top=1in,bottom=1in,right=1in,left=1in]{geometry}'

    rst2latex_call = \
"""\
rst2latex.py --date --documentoptions="letter,10pt" \\
--use-latex-docinfo        --latex-preamble="{}" {} {}\
"""

    date_format = '%A, %B %d, %Y'

    for hw_num in hw_nums:

        text = ""

        # dates
        date_assigned = datetime.datetime.strptime(assigned_dates[hw_num],
                                                   '%Y/%m/%d')
        date_due = date_assigned + datetime.timedelta(days=7)

        root_dir = os.path.abspath(os.path.curdir)
        os.chdir(os.path.join(hw_dir, hw_num))

        files = os.listdir(os.path.curdir)
        part_files = [part for part in files if part.startswith('part')]
        image_files = [part for part in files if part.endswith('png')]

        # join part files together
        for p in sorted(part_files):
            with open(p, 'r') as f:
                text += '\n'
                text += f.read()

        output_file = 'hw-{}.rst'.format(hw_num)

        with open(output_file, 'w') as f:
            f.write(pdf_text.format(hw_num, date_assigned.strftime(date_format),
                                    date_due.strftime(date_format)) + text)

        tex_file = 'hw-{}.tex'.format(hw_num)
        pdf_file = 'hw-{}.pdf'.format(hw_num)
        os.chdir(root_dir)
        with lcd(os.path.join(hw_dir, hw_num)):
            local('pwd')
            local(rst2latex_call.format(preamble, output_file, tex_file))
            local('pdflatex {}'.format(tex_file))
            local('cp {} ../../content/materials/'.format(pdf_file))

        web_dir = 'content/pages/homework'

        if not os.path.exists(web_dir):
            os.makedirs(web_dir)

        img_dir = 'content/images'

        if not os.path.exists(img_dir):
            os.makedirs(img_dir)

        # copy image files over to website
        for im_file in image_files:
            shutil.copy(os.path.join(hw_dir, hw_num, im_file), img_dir)

        with open(os.path.join(web_dir, output_file), 'w') as f:
            text = text.replace('.. image:: ', '.. image:: {attach}/images/')
            f.write(web_text.format(hw_num, date_assigned.strftime(date_format),
                                    date_due.strftime(date_format), hw_num) + text)
