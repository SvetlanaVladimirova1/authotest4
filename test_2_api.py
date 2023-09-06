import requests
import logging
import yaml


with open('testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)
    address = testdata['address_post_API']
    title = testdata['title_API']
    description = testdata['description_API']
    content = testdata['content_API']

S = requests.Session()


def get_my_posts(token):
    response = S.get(url=address, headers={"X-Auth-Token": token})
    if response:
        posts_descriptions = [i['description'] for i in response.json()['data']]
        logging.debug('My posts description')
        return posts_descriptions
    else:
        logging.error("My posts are not available")


def my_post(token):
    post_data = {'title': title, 'description': description, 'content': content}
    response = S.post(url=address, headers={"X-Auth-Token": token}, json=post_data)
    if response:
        logging.debug('Created a new post')
        return response.json()
    else:
        logging.error('Cannot create a post')
        return response


def test_description_api(api_token):
    my_post(api_token)
    assert description in get_my_posts(api_token)