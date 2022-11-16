class DataPoint {
  late int time;
  late double lat;
  late double log;
  late double bpm;

  DataPoint(Map<String, dynamic> pointJson) {
    // parse json point into datastructure
    time = pointJson['time'];
    lat = pointJson['lat'];
    log = pointJson['log'];
    bpm = pointJson['bpm'];
  }
}
