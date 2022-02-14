import os, json, time, requests
from sys import argv

response = False
wp_path = '.'

if len(argv) > 1 :
    wp_path = argv[1]

if len(argv) > 2:
    if (argv[2] == 'True' or argv[2] == '1'):
        response = bool(argv[2])

def get_wp_info(wp_path):
    return '*This readme generated ' + time.strftime('%d.%m.%Y %H:%M:%S') + '<br>Current WordPress version: ' + os.popen('wp core version --path=' + wp_path ).read().strip() + '*\n\n# ' + os.popen('wp option get blogname --path=' + wp_path).read() + '\n*' + os.popen('wp option get blogdescription --path=' + wp_path).read().strip('\n') + '*\n\n' 

def get_plugins_list(wp_path, status='active,inactive', response=False):
    json_response = os.popen('wp plugin list --path=' + wp_path + ' --format=json --fields=name,status,update,version,update_version,title,description --status=' + status)
    output = json.load(json_response)
    plugin_list = ['\nPlugin | Is active? | Version','---|:---:|:---:']

    for plugin in output:
        if (response):
            plink_response = requests.get("https://ru.wordpress.org/plugins/" + plugin['name'])
            if 'shortlink' in plink_response.links:
                md_link = "[" + plugin['title'] + "](" + "https://ru.wordpress.org/plugins/" + plugin['name'] + " '" + plugin['name'] + "')" + (( " *(Available new version: " + plugin['update_version'] + ")*" ) if plugin['update_version'] else '')
            else:
                md_link = plugin['title']
        else:
            md_link = "[" + plugin['title'] + "](" + "https://ru.wordpress.org/plugins/" + plugin['name'] + " '" + plugin['name'] + "')" + (( " *(New version available: " + plugin['update_version'] + ")*" ) if plugin['update_version'] else '')

        md_status = '[:heavy_check_mark:](# "active")' if plugin['status'] == 'active' else '[:x:](# "inactive")'
        md_version = plugin['version']
        md_description = plugin['description']
        plugin_list.append( md_link + "<br>" + md_description.replace('\n', ' ') + "|" + md_status + "|" + md_version + "|" )

    return '\n'.join(plugin_list) + '\n'

def get_themes_list(wp_path, status=False):
    json_response = os.popen('wp theme list --path=' + wp_path + ' --format=json --fields=name,status,update,version,update_version,title ' + (('--status=' + status) if status else ''))
    
    output = json.load(json_response)
    
    theme_list = ['\nTheme | Is active? | Version','---|:---:|:---:']

    for theme in output: 
        theme_list.append( theme['title'] + (( " *(New version available: " + theme['update_version'] + ")*" ) if theme['update_version'] else '') + "|" + theme['status'] + "|" + theme['version'])

    return '\n'.join(theme_list) + '\n'

with open('wp-readme.md', 'w') as outfile:
    outfile.write(get_wp_info(wp_path))
    outfile.write('### Theme: ')
    outfile.write(get_themes_list(wp_path, 'active,parent'))
    outfile.write('### List of plugins: ')
    outfile.write(get_plugins_list(wp_path, 'active', response))