import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel10FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel10FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel10FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel10FlatComponentChunk33

end RHP2Bridge
