import 'package:flutter/material.dart';

void main() => runApp(NavigationDemo());

class NavigationDemo extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Navigation Demo',
      home: FirstScreen(),
    );
  }
}

class FirstScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) => Scaffold(
        appBar: AppBar(title: Text('First Screen')),
        body: Center(
          child: ElevatedButton(
            child: Text('Go to Second Screen'),
            onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => SecondScreen())),
          ),
        ),
      );
}

class SecondScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) => Scaffold(
        appBar: AppBar(title: Text('Second Screen')),
        body: Center(
          child: ElevatedButton(
            child: Text('Go Back'),
            onPressed: () => Navigator.pop(context),
          ),
        ),
      );
}
