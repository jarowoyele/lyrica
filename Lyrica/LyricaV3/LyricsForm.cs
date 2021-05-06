using System.ComponentModel.DataAnnotations;

namespace LyricaV3
{
    public class LyricsForm
    {
        [Required]
        public string Lyrics { get; set; }
    }
}
