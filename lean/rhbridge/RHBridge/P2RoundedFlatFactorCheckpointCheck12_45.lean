import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel12FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel12FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel12FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel12FlatComponentChunk45

end RHP2Bridge
