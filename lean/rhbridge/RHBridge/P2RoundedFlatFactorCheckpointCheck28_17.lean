import RHBridge.P2RoundedFlatFactorCheckpointData28

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FlatComponentChunk17 :
    P2RoundedFactorCheckpointData.panel28FlatEven17 =
      (P2RoundedFactorCheckpointData.panel28TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel28FlatEven17_eq :
    P2RoundedFactorCheckpointData.panel28FlatEven17 =
      (P2RoundedFactorCheckpointData.panel28TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  exact panel28FlatComponentChunk17

end RHP2Bridge
