import 'package:polymer/polymer.dart';

@CustomTag('gm-cycle')
class MyExample extends PolymerElement {
  @observable num daysToAdvance;
  
  bool get applyAuthorStyles => true;
}
