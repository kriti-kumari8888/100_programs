// mongodb_crud.js
// Minimal MongoDB CRUD demo. To run: npm install mongodb && node mongodb_crud.js
// Requires a running MongoDB instance (mongodb://localhost:27017)

const { MongoClient } = require('mongodb');
const url = process.env.MONGO_URL || 'mongodb://localhost:27017';
const dbName = 'fsd_demo';

async function run() {
  const client = new MongoClient(url, { useUnifiedTopology: true });
  await client.connect();
  console.log('Connected to MongoDB');
  const db = client.db(dbName);
  const col = db.collection('users');
  await col.insertOne({name: 'Alice', age: 30});
  const docs = await col.find({}).toArray();
  console.log('Docs:', docs);
  await col.updateOne({name: 'Alice'}, { $set: { age: 31 }});
  await col.deleteMany({age: {$gt: 100}});
  await client.close();
}

run().catch(err => console.error(err));
