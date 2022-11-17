// singlton state manager class

import 'package:find_my_grandpa/data/grandpa_data.dart';

class StateManager {
  // propreties for states

  // private proprties
  static final StateManager _stateManager = StateManager._internal();
  bool _isLoggedIn = false;
  GrandpaData _grandpaData = GrandpaData();

  factory StateManager() {
    return _stateManager;
  }

  StateManager._internal();

  // sets the sate data for the grandpa globally
  void setGrandpaData(GrandpaData g) {
    _grandpaData = g;
  }

  GrandpaData getGrandpa() {
    return _grandpaData;
  }

  void loggedIn() {
    _isLoggedIn = true;
  }
}
