import 'package:flutter/material.dart';

void main() => runApp(CounterApp());

class CounterApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) => MaterialApp(home: CounterHome());
}

class CounterHome extends StatefulWidget {
  @override
  _CounterHomeState createState() => _CounterHomeState();
}

class _CounterHomeState extends State<CounterHome> {
  int _count = 0;

  void _increment() => setState(() => _count++);
  void _decrement() => setState(() => _count--);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Counter App')),
      body: Center(child: Text('Count: \\$_count', style: TextStyle(fontSize: 32))),
      floatingActionButton: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          FloatingActionButton(
            heroTag: 'inc',
            child: Icon(Icons.add),
            onPressed: _increment,
          ),
          SizedBox(height: 8),
          FloatingActionButton(
            heroTag: 'dec',
            child: Icon(Icons.remove),
            onPressed: _decrement,
          ),
        ],
      ),
    );
  }
}
