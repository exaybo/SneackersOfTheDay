using MongoDB.Bson;

namespace SneackersWebViewer.Models
{
    public class Sneacker
    {
        public ObjectId Id { get; set; }
        public string Name { get; set; }
        public string Uri { get; set; }
        public DateTime Date { get; set; }
        public List<string> ImgUriList { get; set; }
    }
}
