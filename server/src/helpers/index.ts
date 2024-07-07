import crypto from 'crypto';
require('dotenv').config();

const SECRET = process.env.SECRET;

// Generates a base64-encoded string of 128 random bytes.
export const random = () => crypto.randomBytes(128).toString('base64');

// Creates an HMAC using SHA-256 and combines the salt, password and a secret value from ENV
export const authentication = (salt: String, password: String) => {
  return crypto
    .createHmac('sha256', [salt, password].join('/'))
    .update(SECRET)
    .digest('hex');
};
