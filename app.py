#!/usr/bin/python

import spotipy
import spotipy.util as util

username = 'swissdanny_67'
scope = 'playlist-modify-private'
client_id = 'de34433c465947d7af723d25cbbfc821'
client_secret ='08f65a7b32774eacb9bd2a8a0a1a5a8c'
redirect_uri = 'http://vps184910.vps.ovh.ca'
cache_path = '/var/www/html/tempoplaylist'

token = util.prompt_for_user_token(
        username,
        scope,
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri)

def get_artist(name):
    results = spotify.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None

def print_results(results):
        for xyz in results['tracks']:
                xyz_id = xyz['id']
                # print xyz_id
                xyz_feat = spotify.audio_features(tracks=[xyz_id])
                # print xyz_feat
                print xyz['name'], '-', xyz['artists'][0]['name']
                print xyz_feat[0]['tempo']

#def get_features(results):
        #features = spotify.audio_features(results['tracks']
        #for track in features['tracks']:
        #       print track['name'], '-', track['tempo']

if token:
        spotify = spotipy.Spotify(auth=token)
        name = 'Clean Cut Kid'
        artist = get_artist(name)
        print artist

        results = spotify.recommendations(
                seed_artists = [artist['id']],
                seed_genres = None, # [genre['alt-indie rock']],
                seed_tracks = None,
                limit = 20,
                country = 'CH',
                min_tempo=163,
                max_tempo=167)
        print_results(results)
        #get_features(results)
else:
        print("Cant get token for", username)
