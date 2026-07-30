import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel10FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel10FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel10FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel10FlatComponentChunk24

end RHP2Bridge
