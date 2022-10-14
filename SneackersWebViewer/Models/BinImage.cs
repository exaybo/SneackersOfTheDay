using MongoDB.Bson;

namespace SneackersWebViewer.Models
{
    public class BinImage
    {
        public ObjectId Id { get; set; }
        public string ImgUri { get; set; }
        public BsonBinaryData ImgBin { get; set; }
    }
}
