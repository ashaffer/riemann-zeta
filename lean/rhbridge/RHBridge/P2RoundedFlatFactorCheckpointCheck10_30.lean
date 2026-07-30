import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel10FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel10FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel10FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel10FlatComponentChunk30

end RHP2Bridge
