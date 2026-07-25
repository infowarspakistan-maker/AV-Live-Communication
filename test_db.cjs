const { initializeApp } = require('firebase-admin/app');
const { getFirestore } = require('firebase-admin/firestore');

initializeApp();
const db = getFirestore('ai-studio-avlivecommunicat-62ef3166-4331-4aa3-87cf-d7384f54afd6');

async function test() {
  const snap = await db.collection('products').limit(1).get();
  console.log('Products:', snap.size);
}
test().catch(console.error);
