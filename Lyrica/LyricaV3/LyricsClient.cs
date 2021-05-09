using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace LyricaV3
{
    public class SearchForm
    {
        [Required]
        public string Query { get; set; }

        //[Required]
        //public string Track { get; set; }
    }
    public class TrackSearchResponse
    {
        public TrackMessage message { get; set; }
    }

    public class TrackMessage
    {
        public THeader header { get; set; }
        public TBody body { get; set; }
    }

    public class THeader
    {
        public int status_code { get; set; }
        public float execute_time { get; set; }
        public int available { get; set; }
    }

    public class TBody
    {
        public Track_List[] track_list { get; set; }
    }

    public class Track_List
    {
        public Track track { get; set; }
    }

    public class Track
    {
        public int track_id { get; set; }
        public string track_name { get; set; }
        public object[] track_name_translation_list { get; set; }
        public int track_rating { get; set; }
        public int commontrack_id { get; set; }
        public int instrumental { get; set; }
        public int _explicit { get; set; }
        public int has_lyrics { get; set; }
        public int has_subtitles { get; set; }
        public int has_richsync { get; set; }
        public int num_favourite { get; set; }
        public int album_id { get; set; }
        public string album_name { get; set; }
        public int artist_id { get; set; }
        public string artist_name { get; set; }
        public string track_share_url { get; set; }
        public string track_edit_url { get; set; }
        public int restricted { get; set; }
        public DateTime updated_time { get; set; }
        public Primary_Genres primary_genres { get; set; }
    }

    public class Primary_Genres
    {
        public Music_Genre_List[] music_genre_list { get; set; }
    }

    public class Music_Genre_List
    {
        public Music_Genre music_genre { get; set; }
    }

    public class Music_Genre
    {
        public int music_genre_id { get; set; }
        public int music_genre_parent_id { get; set; }
        public string music_genre_name { get; set; }
        public string music_genre_name_extended { get; set; }
        public string music_genre_vanity { get; set; }
    }




    public class LyricsSearchResponse
    {
        public LyricsMessage message { get; set; }
    }

    public class LyricsMessage
    {
        public LHeader header { get; set; }
        public LBody body { get; set; }
    }

    public class LHeader
    {
        public int status_code { get; set; }
        public float execute_time { get; set; }
    }

    public class LBody
    {
        public Lyrics lyrics { get; set; }
    }

    public class Lyrics
    {
        public int lyrics_id { get; set; }
        public int _explicit { get; set; }
        public string lyrics_body { get; set; }
        public string script_tracking_url { get; set; }
        public string pixel_tracking_url { get; set; }
        public string lyrics_copyright { get; set; }
        public DateTime updated_time { get; set; }
    }



}
