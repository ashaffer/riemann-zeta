import RHBridge.P2RoundedFactorCheckpointData22

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FactorChunk14 :
    P2RoundedFactorCheckpointData.panel22Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨22, by decide⟩ := by
  decide +kernel

theorem panel22Prefix56_eq :
    P2RoundedFactorCheckpointData.panel22Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk14.1

theorem panel22Prefix57_eq :
    P2RoundedFactorCheckpointData.panel22Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk14.2.1

theorem panel22Prefix58_eq :
    P2RoundedFactorCheckpointData.panel22Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk14.2.2.1

theorem panel22Prefix59_eq :
    P2RoundedFactorCheckpointData.panel22Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk14.2.2.2

end RHP2Bridge
