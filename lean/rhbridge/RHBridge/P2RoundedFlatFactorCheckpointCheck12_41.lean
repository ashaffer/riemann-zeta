import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel12FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel12FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel12FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel12FlatComponentChunk41

end RHP2Bridge
