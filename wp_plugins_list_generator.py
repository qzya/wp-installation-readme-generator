import os, json, requests
from pprint import pprint

def get_plugins_list(wp_path, status='active,inactive', response=False):
    json_response = os.popen('wp plugin list --path=' + wp_path + ' --format=json --fields=name,status,update,version,update_version,title,description --status=' + status)
    output = json.load(json_response)

    plugin_list = ['Plugin | Is active? | Version','---|:---:|:---:']

    with open('wp_list', 'w') as outfile:
        for plugin in output:
            if (response):
                response = requests.get("https://ru.wordpress.org/plugins/" + plugin['name'])
                if 'shortlink' in response.links:
                    md_link = "[" + plugin['title'] + "](" + "https://ru.wordpress.org/plugins/" + plugin['name'] + " '" + plugin['name'] + "')" + (( " *(Available new version: " + plugin['update_version'] + ")*" ) if plugin['update_version'] else '')
                else:
                    md_link = plugin['title']
            else:
                md_link = "[" + plugin['title'] + "](" + "https://ru.wordpress.org/plugins/" + plugin['name'] + " '" + plugin['name'] + "')" + (( " *(New version available: " + plugin['update_version'] + ")*" ) if plugin['update_version'] else '')

            md_status = ':heavy_check_mark:' if plugin['status'] == 'active' else ':x:'
            md_version = plugin['version']
            md_description = plugin['description']
            plugin_list.append( md_link + "<br>" + md_description.replace('\n', ' ') + "|" + md_status + "|" + md_version + "|" )

        joined = '\n'.join(plugin_list)
        outfile.write(joined)

def get_themes_list(wp_path, status=False):
    json_response = os.popen('wp theme list --path=' + wp_path + ' --format=json --fields=name,status,update,version,update_version,title ' + (('--status=' + status) if status else ''))
    
    output = json.load(json_response)

    theme_list = ['Theme | Is active? | Version','---|:---:|:---:']

    for theme in output: 
        # pprint(theme)
        # pprint(theme['title'] + ' ' + theme['status'] + ' ' + theme['update'] + ' ' + (( " *(New version available: " + theme['update_version'] + ")*" ) if theme['update_version'] else ''))
        theme_list.append( theme['title'] + (( " *(New version available: " + theme['update_version'] + ")*" ) if theme['update_version'] else '') + "|" + theme['status'] + "|" + theme['version'])
    
    pprint(theme_list)

# get_plugins_list('/home/qzya/www/lyson.loc', 'active')

get_themes_list('/home/qzya/www/lyson.loc')


