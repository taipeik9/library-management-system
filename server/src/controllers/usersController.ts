import { UserModel } from '../db/users';

/* Queries */
// Get all users
export const getUsers = () => UserModel.find();

// Get User by Email
export const getUserByEmail = (email: String) =>
  UserModel.findOne({ email: email });

// Get User by session Token
export const getUserBySessionToken = (sessionToken: String) =>
  UserModel.findOne({ 'authentication.sessionToken': sessionToken });

// Get User by _id
export const getUserById = (id: String) => UserModel.findById(id);

/* Modifiers */
// Create User
export const createUser = (values: Record<string, any>) =>
  new UserModel(values).save().then((user) => user.toObject());

// Delete User by _id
export const deleteUserById = (id: String) => UserModel.findByIdAndDelete(id);

// Update User by _id
export const updateUserById = (id: String, values: Record<string, any>) =>
  UserModel.findByIdAndUpdate(id, values);
