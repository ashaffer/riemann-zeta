import RHBridge.P2RoundedFlatFactorCheckpointData28

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FlatComponentChunk2 :
    P2RoundedFactorCheckpointData.panel28FlatEven2 =
      (P2RoundedFactorCheckpointData.panel28TruncatedEvenComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel28FlatEven2_eq :
    P2RoundedFactorCheckpointData.panel28FlatEven2 =
      (P2RoundedFactorCheckpointData.panel28TruncatedEvenComponents).get ⟨2, by decide⟩ := by
  exact panel28FlatComponentChunk2

end RHP2Bridge
