from invoke import task


@task(aliases=['s'])
def setup(c, version=None):
    """
    Setup dev environment, requires conda
    """
    version = version or '3.9'
    suffix = '' if version == '3.9' else version.replace('.', '')
    env_name = f'k2s{suffix}'

    c.run(f'conda create --name {env_name} python={version} --yes')
    c.run('eval "$(conda shell.bash hook)" '
          f'&& conda activate {env_name} '
          '&& pip install --editable .[dev]')

    print(f'Done! Activate your environment with:\nconda activate {env_name}')


@task(aliases=['sj'])
def setup_jupyter(c, version=None):
    """
    Setup a clean environment with jupyterlab for testing
    """
    version = version or '3.8'
    env_name = 'k2s-jupyter'
    c.run(f'conda create --name {env_name} python={version} --yes')
    c.run('eval "$(conda shell.bash hook)" '
          f'&& conda activate {env_name} '
          '&& pip install jupyterlab')
    print(f'Done! Activate your environment with:\nconda activate {env_name}')


@task(aliases=['v'])
def version(c):
    """Release a new version
    """
    from pkgmt import versioneer
    versioneer.version(project_root='.', tag=True)


@task(aliases=['r'])
def release(c, tag, production=True):
    """Upload to PyPI
    """
    from pkgmt import versioneer
    versioneer.upload(tag, production=production)
