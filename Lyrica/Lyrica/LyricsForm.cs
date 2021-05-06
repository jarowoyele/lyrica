using System.ComponentModel.DataAnnotations;

namespace Lyrica
{
    public class LyricsForm
    {
        [Required]
        public string Lyrics { get; set; }
    }
}
