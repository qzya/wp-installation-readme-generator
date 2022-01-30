import os, json, requests
from pprint import pprint

def get_plugins_list(wp_path, status='active,inactive', response=False):
    json_response = os.popen('wp plugin list --path=' + wp_path + ' --format=json --fields=name,status,update,version,update_version,title,description --status=' + status)
    output = json.load(json_response)

    plugin_list = ['Plugin | Is active? | Version','---|:---:|:---:']

    for plugin in output:
        if (response):
            response = requests.get("https://ru.wordpress.org/plugins/" + plugin['name'])
            if 'shortlink' in response.links:
                md_link = "[" + plugin['title'] + "](" + "https://ru.wordpress.org/plugins/" + plugin['name'] + " '" + plugin['name'] + "')" + (( " *(Available new version: " + plugin['update_version'] + ")*" ) if plugin['update_version'] else '')
            else:
                md_link = plugin['title']
        else:
            md_link = "[" + plugin['title'] + "](" + "https://ru.wordpress.org/plugins/" + plugin['name'] + " '" + plugin['name'] + "')" + (( " *(New version available: " + plugin['update_version'] + ")*" ) if plugin['update_version'] else '')

        md_status = '[:heavy_check_mark:](# "active")' if plugin['status'] == 'active' else '[:x:](# "inactive")'
        md_version = plugin['version']
        md_description = plugin['description']
        plugin_list.append( md_link + "<br>" + md_description.replace('\n', ' ') + "|" + md_status + "|" + md_version + "|" )

    return '\n'.join(plugin_list)

def get_themes_list(wp_path, status=False):
    json_response = os.popen('wp theme list --path=' + wp_path + ' --format=json --fields=name,status,update,version,update_version,title ' + (('--status=' + status) if status else ''))
    
    output = json.load(json_response)

    theme_list = ['Theme | Is active? | Version','---|:---:|:---:']

    for theme in output: 
        theme_list.append( theme['title'] + (( " *(New version available: " + theme['update_version'] + ")*" ) if theme['update_version'] else '') + "|" + theme['status'] + "|" + theme['version'])
    
    return '\n'.join(theme_list)

with open('wp_info.md', 'w') as outfile:

    outfile.write(get_themes_list('/home/qzya/www/lyson.loc', 'active,parent'))
    outfile.write('\n---\n')
    outfile.write(get_plugins_list('/home/qzya/www/lyson.loc', 'active'))