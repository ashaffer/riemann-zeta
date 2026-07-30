import RHBridge.P2RoundedFlatFactorCheckpointData28

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FlatComponentChunk4 :
    P2RoundedFactorCheckpointData.panel28FlatEven4 =
      (P2RoundedFactorCheckpointData.panel28TruncatedEvenComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel28FlatEven4_eq :
    P2RoundedFactorCheckpointData.panel28FlatEven4 =
      (P2RoundedFactorCheckpointData.panel28TruncatedEvenComponents).get ⟨4, by decide⟩ := by
  exact panel28FlatComponentChunk4

end RHP2Bridge
