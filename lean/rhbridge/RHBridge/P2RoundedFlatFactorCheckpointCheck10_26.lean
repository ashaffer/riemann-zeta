import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel10FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel10FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel10FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel10FlatComponentChunk26

end RHP2Bridge
