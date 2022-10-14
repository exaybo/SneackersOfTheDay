using MongoDB.Bson;
using MongoDB.Bson.Serialization;
using MongoDB.Driver;
using SneackersWebViewer.Models;
using System;

namespace SneackersWebViewer.Controllers
{
    public interface ISneackersContext
    {
        List<Sneacker> GetAllSneackers();
        List<Attempt> GetAllAttempts();
        string GetBase64Image(string uriKey);
    }


    public class SneackersContext : ISneackersContext, IDisposable
    {
        MongoClient dbClient;
        public SneackersContext()
        {
            dbClient = new MongoClient("mongodb://host.docker.internal:27017");

        }

        public void Dispose()
        {
            
        }

        public string GetBase64Image(string uriKey)
        {
            string ret = "";
            var binImagesCol = dbClient.GetDatabase("sneackers_db").GetCollection<BinImage>("binimages");
            var filter = Builders<BinImage>.Filter.Eq("ImgUri", uriKey);
            var binImg = binImagesCol.Find<BinImage>(filter).FirstOrDefault();
            
            if (binImg != null && binImg.ImgBin != null)
            {
                ret = "data:image/png;base64," + Convert.ToBase64String(binImg.ImgBin.AsByteArray, 0, binImg.ImgBin.AsByteArray.Length);
            }
            return ret;
        }

        public List<Attempt> GetAllAttempts()
        {
            var attemptsCol = dbClient.GetDatabase("sneackers_db").GetCollection<Attempt>("attempts");
            var attempts = attemptsCol.Find<Attempt>(new BsonDocument()).ToList();
            return attempts;
        }

        public List<Sneacker> GetAllSneackers()
        {           
            var sneakersCol = dbClient.GetDatabase("sneackers_db").GetCollection<Sneacker>("sneakers");
            var sneackers = sneakersCol.Find<Sneacker>(new BsonDocument()).ToList();
            return sneackers;
        }

        
    }
}

// run
// docker run --rm sneackers_crowler

// run mongo
// docker run --rm -d -p 27017:27017 mongo