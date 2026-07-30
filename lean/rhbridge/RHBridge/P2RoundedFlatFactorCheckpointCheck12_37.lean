import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk37 :
    P2RoundedFactorCheckpointData.panel12FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel12FlatOdd13_eq :
    P2RoundedFactorCheckpointData.panel12FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨13, by decide⟩ := by
  exact panel12FlatComponentChunk37

end RHP2Bridge
