import RHBridge.P2RoundedFactorCheckpointData28

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FactorChunk15 :
    P2RoundedFactorCheckpointData.panel28Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨28, by decide⟩ := by
  decide +kernel

theorem panel28Prefix60_eq :
    P2RoundedFactorCheckpointData.panel28Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk15.1

theorem panel28Prefix61_eq :
    P2RoundedFactorCheckpointData.panel28Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk15.2.1

theorem panel28Prefix62_eq :
    P2RoundedFactorCheckpointData.panel28Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk15.2.2.1

theorem panel28Prefix63_eq :
    P2RoundedFactorCheckpointData.panel28Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk15.2.2.2

end RHP2Bridge
