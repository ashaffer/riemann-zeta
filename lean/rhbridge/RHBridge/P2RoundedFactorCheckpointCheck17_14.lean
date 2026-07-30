import RHBridge.P2RoundedFactorCheckpointData17

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FactorChunk14 :
    P2RoundedFactorCheckpointData.panel17Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨17, by decide⟩ := by
  decide +kernel

theorem panel17Prefix56_eq :
    P2RoundedFactorCheckpointData.panel17Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk14.1

theorem panel17Prefix57_eq :
    P2RoundedFactorCheckpointData.panel17Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk14.2.1

theorem panel17Prefix58_eq :
    P2RoundedFactorCheckpointData.panel17Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk14.2.2.1

theorem panel17Prefix59_eq :
    P2RoundedFactorCheckpointData.panel17Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk14.2.2.2

end RHP2Bridge
