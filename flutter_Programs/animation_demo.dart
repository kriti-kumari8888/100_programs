import 'package:flutter/material.dart';

void main() => runApp(AnimationDemo());

class AnimationDemo extends StatelessWidget {
  @override
  Widget build(BuildContext context) => MaterialApp(home: AnimatedBoxPage());
}

class AnimatedBoxPage extends StatefulWidget {
  @override
  _AnimatedBoxPageState createState() => _AnimatedBoxPageState();
}

class _AnimatedBoxPageState extends State<AnimatedBoxPage> {
  bool _big = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Animation Demo')),
      body: Center(
        child: GestureDetector(
          onTap: () => setState(() => _big = !_big),
          child: AnimatedContainer(
            duration: Duration(milliseconds: 500),
            width: _big ? 200 : 100,
            height: _big ? 200 : 100,
            color: _big ? Colors.blue : Colors.green,
            curve: Curves.easeInOut,
            child: Center(child: Text('Tap me', style: TextStyle(color: Colors.white))),
          ),
        ),
      ),
    );
  }
}
