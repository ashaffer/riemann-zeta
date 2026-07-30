import RHBridge.P2RoundedFlatFactorCheckpointData28

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel28FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel28FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel28FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel28FlatComponentChunk26

end RHP2Bridge
