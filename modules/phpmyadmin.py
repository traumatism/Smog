import requests

from smog.abstract.module import ModuleBase
from smog.database.types.url import URL

from requests.packages.urllib3 import disable_warnings

PHPMYADMIN_PATHS = (
    '', 'myadmin/', 'PMA', 'PMA/', 'PMA/index.php',
    'PMA2/index.php', '__pma___', 'admin/pMA/',
    'admin/pma/', 'admin/PMA/index.php', 'admin/pma/index.php',
    'administrator/PMA/', 'administrator/pma/',
    'mysql/pMA/', 'mysql/pma/', 'PMA', 'pma', 'pma-old/index.php',
    'PMA/', 'pma/', 'PMA/index.php', 'pma/index.php', 'pma/scripts/setup.php',
    'PMA2/index.php', 'PMA2005', 'pma2005', 'PMA2005/', 'pma2005/',
    'PMA2009/', 'pma2009/', 'PMA2011/', 'pma2011/', 'PMA2012/', 'pma2012/',
    'PMA2013/', 'pma2013/', 'PMA2014/', 'pma2014/', 'PMA2015/', 'pma2015/',
    'PMA2016/', 'pma2016/', 'PMA2017/', 'pma2017/', 'PMA2018/', 'pma2018/',
    'pma4/', 'pmadmin', 'pmadmin/', 'pmamy/index.php', 'pmamy2/index.php',
    'sql/phpmanager/', '.tools/phpMyAdmin/', '.tools/phpMyAdmin/current/',
    '2phpmyadmin/', '_LPHPMYADMIN/', '_phpmyadmin', '_phpmyadmin/', 'admin/phpMyAdmin',
    'admin/phpMyAdmin/', 'admin/phpmyadmin/', 'admin/phpMyAdmin/index.php',
    'admin/phpmyadmin/index.php', 'admin/phpmyadmin2/index.php', 'administrator/phpMyAdmin/',
    'administrator/phpmyadmin/', 'claroline/phpMyAdmin/index.php', 'database/phpMyAdmin/',
    'database/phpmyadmin/', 'database/phpMyAdmin2/', 'database/phpmyadmin2/', 'db/phpMyAdmin-2/',
    'db/phpMyAdmin-3/', 'db/phpMyAdmin/', 'db/phpmyadmin/', 'db/phpMyAdmin2/', 'db/phpmyadmin2/',
    'db/phpMyAdmin3/', 'db/phpmyadmin3/', 'phpmyadmin/ChangeLog', 'phpmyadmin/doc/html/index.html',
    'phpmyadmin/docs/html/index.html', 'phpmyadmin/README', 'phpMyAdmin', 'phpmyadmin', 'phpmyadmin!!',
    'phpMyAdmin-2', 'phpMyAdmin-2.10.0/', 'phpMyAdmin-2.10.1/', 'phpMyAdmin-2.10.2/', 'phpMyAdmin-2.10.3/',
    'phpMyAdmin-2.11.0/', 'phpMyAdmin-2.11.1/', 'phpMyAdmin-2.11.10/', 'phpMyAdmin-2.11.2/', 'phpMyAdmin-2.11.3/',
    'phpMyAdmin-2.11.4/', 'phpMyAdmin-2.11.5.1-all-languages/', 'phpMyAdmin-2.11.5/', 'phpMyAdmin-2.11.6-all-languages/',
    'phpMyAdmin-2.11.6/', 'phpMyAdmin-2.11.7.1-all-languages-utf-8-only/', 'phpMyAdmin-2.11.7.1-all-languages/',
    'phpMyAdmin-2.11.7/', 'phpMyAdmin-2.11.8.1-all-languages-utf-8-only/', 'phpMyAdmin-2.11.8.1-all-languages/',
    'phpMyAdmin-2.11.8.1/', 'phpMyAdmin-2.11.9/', 'phpMyAdmin-2.2.3', 'phpMyAdmin-2.2.3/', 'phpMyAdmin-2.2.6',
    'phpMyAdmin-2.2.6/', 'phpMyAdmin-2.5.1', 'phpMyAdmin-2.5.1/', 'phpMyAdmin-2.5.4', 'phpMyAdmin-2.5.4/',
    'phpMyAdmin-2.5.5', 'phpMyAdmin-2.5.5-pl1', 'phpMyAdmin-2.5.5-pl1/', 'phpMyAdmin-2.5.5-rc1',
    'phpMyAdmin-2.5.5-rc1/', 'phpMyAdmin-2.5.5-rc2', 'phpMyAdmin-2.5.5-rc2/', 'phpMyAdmin-2.5.5/',
    'phpMyAdmin-2.5.6', 'phpMyAdmin-2.5.6-rc1', 'phpMyAdmin-2.5.6-rc1/', 'phpMyAdmin-2.5.6-rc2',
    'phpMyAdmin-2.5.6-rc2/', 'phpMyAdmin-2.5.6/', 'phpMyAdmin-2.5.7', 'phpMyAdmin-2.5.7-pl1',
    'phpMyAdmin-2.5.7-pl1/', 'phpMyAdmin-2.5.7/', 'phpMyAdmin-2.6.0', 'phpMyAdmin-2.6.0-alpha',
    'phpMyAdmin-2.6.0-alpha/', 'phpMyAdmin-2.6.0-alpha2', 'phpMyAdmin-2.6.0-alpha2/', 'phpMyAdmin-2.6.0-beta1',
    'phpMyAdmin-2.6.0-beta1/', 'phpMyAdmin-2.6.0-beta2', 'phpMyAdmin-2.6.0-beta2/', 'phpMyAdmin-2.6.0-pl1',
    'phpMyAdmin-2.6.0-pl1/', 'phpMyAdmin-2.6.0-pl2', 'phpMyAdmin-2.6.0-pl2/', 'phpMyAdmin-2.6.0-pl3',
    'phpMyAdmin-2.6.0-pl3/', 'phpMyAdmin-2.6.0-rc1', 'phpMyAdmin-2.6.0-rc1/', 'phpMyAdmin-2.6.0-rc2',
    'phpMyAdmin-2.6.0-rc2/', 'phpMyAdmin-2.6.0-rc3', 'phpMyAdmin-2.6.0-rc3/', 'phpMyAdmin-2.6.0/',
    'phpMyAdmin-2.6.1', 'phpMyAdmin-2.6.1-pl1', 'phpMyAdmin-2.6.1-pl1/', 'phpMyAdmin-2.6.1-pl2',
    'phpMyAdmin-2.6.1-pl2/', 'phpMyAdmin-2.6.1-pl3', 'phpMyAdmin-2.6.1-pl3/', 'phpMyAdmin-2.6.1-rc1',
    'phpMyAdmin-2.6.1-rc1/', 'phpMyAdmin-2.6.1-rc2', 'phpMyAdmin-2.6.1-rc2/', 'phpMyAdmin-2.6.1/',
    'phpMyAdmin-2.6.2', 'phpMyAdmin-2.6.2-beta1', 'phpMyAdmin-2.6.2-beta1/', 'phpMyAdmin-2.6.2-pl1',
    'phpMyAdmin-2.6.2-pl1/', 'phpMyAdmin-2.6.2-rc1', 'phpMyAdmin-2.6.2-rc1/', 'phpMyAdmin-2.6.2/',
    'phpMyAdmin-2.6.3', 'phpMyAdmin-2.6.3-pl1', 'phpMyAdmin-2.6.3-pl1/', 'phpMyAdmin-2.6.3-rc1',
    'phpMyAdmin-2.6.3-rc1/', 'phpMyAdmin-2.6.3/', 'phpMyAdmin-2.6.4', 'phpMyAdmin-2.6.4-pl1',
    'phpMyAdmin-2.6.4-pl1/', 'phpMyAdmin-2.6.4-pl2', 'phpMyAdmin-2.6.4-pl2/', 'phpMyAdmin-2.6.4-pl3',
    'phpMyAdmin-2.6.4-pl3/', 'phpMyAdmin-2.6.4-pl4', 'phpMyAdmin-2.6.4-pl4/', 'phpMyAdmin-2.6.4-rc1',
    'phpMyAdmin-2.6.4-rc1/', 'phpMyAdmin-2.6.4/', 'phpMyAdmin-2.7.0', 'phpMyAdmin-2.7.0-beta1', 'phpMyAdmin-2.7.0-beta1/',
    'phpMyAdmin-2.7.0-pl1', 'phpMyAdmin-2.7.0-pl1/', 'phpMyAdmin-2.7.0-pl2', 'phpMyAdmin-2.7.0-pl2/', 'phpMyAdmin-2.7.0-rc1',
    'phpMyAdmin-2.7.0-rc1/', 'phpMyAdmin-2.7.0/', 'phpMyAdmin-2.8.0', 'phpMyAdmin-2.8.0-beta1', 'phpMyAdmin-2.8.0-beta1/',
    'phpMyAdmin-2.8.0-rc1', 'phpMyAdmin-2.8.0-rc1/', 'phpMyAdmin-2.8.0-rc2', 'phpMyAdmin-2.8.0-rc2/', 'phpMyAdmin-2.8.0.1',
    'phpMyAdmin-2.8.0.1/', 'phpMyAdmin-2.8.0.2', 'phpMyAdmin-2.8.0.2/', 'phpMyAdmin-2.8.0.3', 'phpMyAdmin-2.8.0.3/',
    'phpMyAdmin-2.8.0.4', 'phpMyAdmin-2.8.0.4/', 'phpMyAdmin-2.8.0/', 'phpMyAdmin-2.8.1', 'phpMyAdmin-2.8.1-rc1',
    'phpMyAdmin-2.8.1-rc1/', 'phpMyAdmin-2.8.1/', 'phpMyAdmin-2.8.2', 'phpMyAdmin-2.8.2/', 'phpMyAdmin-2/', 'phpMyAdmin-3.0.0/',
    'phpMyAdmin-3.0.1/', 'phpMyAdmin-3.1.0/', 'phpMyAdmin-3.1.1/', 'phpMyAdmin-3.1.2/', 'phpMyAdmin-3.1.3/', 'phpMyAdmin-3.1.4/',
    'phpMyAdmin-3.1.5/', 'phpMyAdmin-3.2.0/', 'phpMyAdmin-3.2.1/', 'phpMyAdmin-3.2.2/', 'phpMyAdmin-3.2.3/', 'phpMyAdmin-3.2.4/',
    'phpMyAdmin-3.2.5/', 'phpMyAdmin-3.3.0/', 'phpMyAdmin-3.3.1/', 'phpMyAdmin-3.3.2-rc1/', 'phpMyAdmin-3.3.2/', 'phpMyAdmin-3.3.3-rc1/',
    'phpMyAdmin-3.3.3/', 'phpMyAdmin-3.3.4-rc1/', 'phpMyAdmin-3.3.4/', 'phpMyAdmin-3/', 'phpMyAdmin-4/', 'phpmyadmin-old',
    'phpmyadmin-old/index.php', 'phpMyAdmin.old/index.php', 'phpMyAdmin/', 'phpMyadmin/', 'phpmyAdmin/', 'phpmyadmin/',
    'phpMyAdmin/index.php', 'phpmyadmin/index.php', 'phpMyAdmin/phpMyAdmin/index.php', 'phpmyadmin/phpmyadmin/index.php',
    'phpMyAdmin/scripts/setup.php', 'phpmyadmin/scripts/setup.php', 'phpMyAdmin0/', 'phpmyadmin0/', 'phpmyadmin0/index.php',
    'phpMyAdmin1/', 'phpmyadmin1/', 'phpmyadmin1/index.php', 'phpMyAdmin2', 'phpmyadmin2', 'phpMyAdmin2/', 'phpmyadmin2/',
    'phpmyadmin2/index.php', 'phpmyadmin2011/', 'phpmyadmin2012/', 'phpmyadmin2013/', 'phpmyadmin2014/', 'phpmyadmin2015/',
    'phpmyadmin2016/', 'phpmyadmin2017/', 'phpmyadmin2018/', 'phpmyadmin3', 'phpMyAdmin3/', 'phpmyadmin3/', 'phpMyAdmin4/',
    'phpmyadmin4/', 'phpMyadmin_bak/index.php', 'phpMyAdminBackup/', 'phpMyAdminold/index.php', 'sql/phpMyAdmin/', 'sql/phpMyAdmin2/',
    'sql/phpmyadmin2/', 'tools/phpMyAdmin/index.php', 'typo3/phpmyadmin/', 'typo3/phpmyadmin/index.php', 'typo3/phpmyadmin/scripts/setup.php',
    'uber/phpMyAdmin/', 'uber/phpMyAdminBackup/', 'web/phpMyAdmin/', 'web/phpMyAdmin/index.php', 'web/phpMyAdmin/scripts/setup.php',
    'www/phpMyAdmin/index.php', 'xampp/phpmyadmin/', 'xampp/phpmyadmin/index.php', 'xampp/phpmyadmin/scripts/setup.php', 'xphpMyAdmin/'
)

disable_warnings()


class PhpMyAdmin(ModuleBase):

    name = "phpmyadmin"
    description = "Search for phpmyadmin in the URLs"
    author = "toastakerman"

    def subaction(self, target):
        for path in PHPMYADMIN_PATHS:
            try:
                response = requests.get("%s/%s" % (target, path), verify=False, timeout=5)
            except:
                continue

            if "phpmyadmin" in response.text.lower() and response.status_code is not 404:
                self.database.insert_data(URL(response.url))

    def execute(self):
        targets = self.database.select_data("urls") or {}
        for _, target in targets.items():
            self.respect_threads_run((target,))
