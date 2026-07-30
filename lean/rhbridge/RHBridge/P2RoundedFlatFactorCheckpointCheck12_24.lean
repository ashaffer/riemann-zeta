import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel12FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel12FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel12FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel12FlatComponentChunk24

end RHP2Bridge
