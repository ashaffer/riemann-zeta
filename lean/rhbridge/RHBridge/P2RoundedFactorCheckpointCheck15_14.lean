import RHBridge.P2RoundedFactorCheckpointData15

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FactorChunk14 :
    P2RoundedFactorCheckpointData.panel15Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨15, by decide⟩ := by
  decide +kernel

theorem panel15Prefix56_eq :
    P2RoundedFactorCheckpointData.panel15Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk14.1

theorem panel15Prefix57_eq :
    P2RoundedFactorCheckpointData.panel15Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk14.2.1

theorem panel15Prefix58_eq :
    P2RoundedFactorCheckpointData.panel15Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk14.2.2.1

theorem panel15Prefix59_eq :
    P2RoundedFactorCheckpointData.panel15Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk14.2.2.2

end RHP2Bridge
