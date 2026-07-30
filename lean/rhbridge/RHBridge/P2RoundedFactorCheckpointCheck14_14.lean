import RHBridge.P2RoundedFactorCheckpointData14

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FactorChunk14 :
    P2RoundedFactorCheckpointData.panel14Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨14, by decide⟩ := by
  decide +kernel

theorem panel14Prefix56_eq :
    P2RoundedFactorCheckpointData.panel14Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk14.1

theorem panel14Prefix57_eq :
    P2RoundedFactorCheckpointData.panel14Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk14.2.1

theorem panel14Prefix58_eq :
    P2RoundedFactorCheckpointData.panel14Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk14.2.2.1

theorem panel14Prefix59_eq :
    P2RoundedFactorCheckpointData.panel14Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk14.2.2.2

end RHP2Bridge
