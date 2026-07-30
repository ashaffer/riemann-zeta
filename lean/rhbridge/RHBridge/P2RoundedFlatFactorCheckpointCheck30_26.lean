import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel30FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel30FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel30FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel30FlatComponentChunk26

end RHP2Bridge
