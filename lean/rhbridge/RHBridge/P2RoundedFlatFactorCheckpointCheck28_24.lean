import RHBridge.P2RoundedFlatFactorCheckpointData28

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel28FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel28FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel28FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel28FlatComponentChunk24

end RHP2Bridge
