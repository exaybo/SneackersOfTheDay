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