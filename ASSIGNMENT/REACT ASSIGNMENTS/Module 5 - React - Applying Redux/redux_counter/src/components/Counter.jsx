import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { incrementCounter, decrementCounter } from '../store/actions';

const Counter = () => {
    const count = useSelector(state => state.count);
    const dispatch = useDispatch();

    return (
        <div>
            <h1>Counter: {count}</h1>
            <button onClick={() => dispatch(incrementCounter())}>Increment</button>
            <button onClick={() => dispatch(decrementCounter())}>Decrement</button>
        </div>
    );
};

export default Counter;