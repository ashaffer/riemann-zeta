import RHBridge.P2RoundedFactorCheckpointData28

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FactorChunk9 :
    P2RoundedFactorCheckpointData.panel28Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨28, by decide⟩ := by
  decide +kernel

theorem panel28Prefix36_eq :
    P2RoundedFactorCheckpointData.panel28Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk9.1

theorem panel28Prefix37_eq :
    P2RoundedFactorCheckpointData.panel28Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk9.2.1

theorem panel28Prefix38_eq :
    P2RoundedFactorCheckpointData.panel28Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk9.2.2.1

theorem panel28Prefix39_eq :
    P2RoundedFactorCheckpointData.panel28Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk9.2.2.2

end RHP2Bridge
