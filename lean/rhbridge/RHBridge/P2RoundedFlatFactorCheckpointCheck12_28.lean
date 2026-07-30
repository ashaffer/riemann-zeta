import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk28 :
    P2RoundedFactorCheckpointData.panel12FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel12FlatOdd4_eq :
    P2RoundedFactorCheckpointData.panel12FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨4, by decide⟩ := by
  exact panel12FlatComponentChunk28

end RHP2Bridge
