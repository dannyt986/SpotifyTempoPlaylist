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
