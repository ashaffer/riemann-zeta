import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel12FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel12FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel12FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel12FlatComponentChunk33

end RHP2Bridge
