import RHBridge.P2RoundedFlatFactorCheckpointData28

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FlatComponentChunk6 :
    P2RoundedFactorCheckpointData.panel28FlatEven6 =
      (P2RoundedFactorCheckpointData.panel28TruncatedEvenComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel28FlatEven6_eq :
    P2RoundedFactorCheckpointData.panel28FlatEven6 =
      (P2RoundedFactorCheckpointData.panel28TruncatedEvenComponents).get ⟨6, by decide⟩ := by
  exact panel28FlatComponentChunk6

end RHP2Bridge
