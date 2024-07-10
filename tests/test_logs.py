import pytest
import colorama
from thefuck import logs


def test_color(settings):
    settings.no_colors = False
    assert logs.color('red') == 'red'
    settings.no_colors = True
    assert logs.color('red') == ''


@pytest.mark.usefixtures('no_colors')
@pytest.mark.parametrize('debug, stderr', [
    (True, 'DEBUG: test\n'),
    (False, '')])
def test_debug(capsys, settings, debug, stderr):
    settings.debug = debug
    logs.debug('test')
    assert capsys.readouterr() == ('', stderr)

def test_failed(capfd):
    logs.failed('test')
    out, err = capfd.readouterr()
    logs.print_failed_coverage()
    assert u'{red}test{reset}\n'.format(red=logs.color(colorama.Fore.RED),reset=colorama.Style.RESET_ALL) == err

def test_failed_no_message(capfd):
    logs.failed()
    out2, err2 = capfd.readouterr()
    logs.print_failed_coverage()
    assert 'No message [WARN]' == err2


'''def test_warn(capfd):
  #  logs.warn('test')
   # out, err = capfd.readouterr()
    logs.print_warn_coverage()
    #assert u'{warn}[WARN] test{reset}\n'.format(warn=logs.color(colorama.Back.RED + colorama.Fore.WHITE+ colorama.Style.BRIGHT),reset=logs.color(colorama.Style.RESET_ALL)) == err
def test_warn_no_message(capfd):
    logs.warn()
    out, err = capfd.readouterr()
    logs.print_warn_coverage()
    assert err == 'No title[WARN]'
'''