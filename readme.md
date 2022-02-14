# WordPress installation readme generator

Python script generates github readme markdown file for WordPress site repositories (see [wp-readme.md](wp-readme.md) for example).<br>
Creates pretty plugins and themes lists.

:exclamation: Needs installed python, [wp-cli](https://github.com/wp-cli/wp-cli) and working WordPress installation (with connected and working database). :exclamation:

### Usage:

launch script in WordPress directory:<br>
`python wp_readme_gen.py`

or launch anywhere with full path to WordPress installation as argument:<br>
`python wp_readme_gen.py '/home/user/www/yoursite.local'`

The output file will appear in the same directory as the script.

### List of plugins example: 
Plugin | Is active? | Version
---|:---:|:---:
[Advanced Cron Manager](https://ru.wordpress.org/plugins/advanced-cron-manager 'advanced-cron-manager') *(New version available: 2.4.2)*<br>View, pause, remove, edit and add WP Cron events.|[:heavy_check_mark:](# "active")|2.4.1|
[Advanced Custom Fields](https://ru.wordpress.org/plugins/advanced-custom-fields 'advanced-custom-fields') *(New version available: 5.11.4)*<br>Customize WordPress with powerful, professional and intuitive fields.|[:heavy_check_mark:](# "active")|5.10.2|
[Advanced Editor Tools (previously TinyMCE Advanced)](https://ru.wordpress.org/plugins/tinymce-advanced 'tinymce-advanced')<br>Extends and enhances the block editor (Gutenberg) and the classic editor (TinyMCE).|[:heavy_check_mark:](# "active")|5.6.0|
[All In One WP Security](https://ru.wordpress.org/plugins/all-in-one-wp-security-and-firewall 'all-in-one-wp-security-and-firewall') *(New version available: 4.4.10)*<br>All round best WordPress security plugin!|[:heavy_check_mark:](# "active")|4.4.9|
[Contact Form 7](https://ru.wordpress.org/plugins/contact-form-7 'contact-form-7') *(New version available: 5.5.5)*<br>Just another contact form plugin. Simple but flexible.|[:heavy_check_mark:](# "active")|5.4.2|
[Disable Gutenberg](https://ru.wordpress.org/plugins/disable-gutenberg 'disable-gutenberg') *(New version available: 2.6)*<br>Disables Gutenberg Block Editor and restores the Classic Editor and original Edit Post screen. Provides options to enable on specific post types, user roles, and more.|[:heavy_check_mark:](# "active")|2.5.1|
[Meta modern cleaner](https://ru.wordpress.org/plugins/meta-modern-cleaner 'meta-modern-cleaner')<br>Simple plugin for clean meta data in posts (and CPTs)|[:heavy_check_mark:](# "active")|0.1.0|
[Query Monitor](https://ru.wordpress.org/plugins/query-monitor 'query-monitor')<br>The Developer Tools Panel for WordPress.|[:heavy_check_mark:](# "active")|3.8.2|
[WooCommerce](https://ru.wordpress.org/plugins/woocommerce 'woocommerce') *(New version available: 6.2.0)*<br>An eCommerce toolkit that helps you sell anything. Beautifully.|[:heavy_check_mark:](# "active")|5.7.1|
[WP Mail SMTP](https://ru.wordpress.org/plugins/wp-mail-smtp 'wp-mail-smtp') *(New version available: 3.2.1)*<br>Reconfigures the <code>wp_mail()</code> function to use Gmail/Mailgun/SendGrid/SMTP instead of the default <code>mail()</code> and creates an options page to manage the settings.|[:heavy_check_mark:](# "active")|3.1.0|