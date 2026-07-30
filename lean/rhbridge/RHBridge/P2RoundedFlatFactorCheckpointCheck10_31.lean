import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel10FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel10FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel10FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel10FlatComponentChunk31

end RHP2Bridge
